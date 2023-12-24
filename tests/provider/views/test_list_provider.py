import pytest

from provider.models.provider import Provider
from tests.provider.factories import (
    ProviderFactory,
    CustomerFactory,
    ContactFactory,
    ProductFactory,
    ProductToProviderFactory,
)


@pytest.mark.django_db
class TestGet:
    def test_get_providers(self, api_client):
        provider_1 = ProviderFactory(name='First level', provider=None, level=Provider.ProviderLevelChoices.FIRST_LEVEL)
        provider_2 = CustomerFactory(
            name='Second level', provider=provider_1, level=Provider.ProviderLevelChoices.SECOND_LEVEL
        )
        provider_3 = CustomerFactory(
            name='Third level', provider=provider_2, level=Provider.ProviderLevelChoices.THIRD_LEVEL
        )
        CustomerFactory(name='Fourth level', provider=provider_3, level=Provider.ProviderLevelChoices.FOURTH_LEVEL)

        response = api_client.get('/api/providers/')

        assert response.status_code == 200

    def test_get_providers_with_contacts_products(self, api_client):
        provider_1 = ProviderFactory(name='First level', provider=None, level=Provider.ProviderLevelChoices.FIRST_LEVEL)
        provider_2 = CustomerFactory(
            name='Second level', provider=provider_1, level=Provider.ProviderLevelChoices.SECOND_LEVEL
        )
        ContactFactory(city='Minsk', provider=provider_1)
        ContactFactory(city='Grodno', provider=provider_1)
        ContactFactory(city='Brest', provider=provider_2)

        product1 = ProductFactory(name='Product')
        product2 = ProductFactory(name='Another Product')

        ProductToProviderFactory(product=product1, provider=provider_1)
        ProductToProviderFactory(product=product2, provider=provider_2)

        response = api_client.get('/api/providers/')

        assert response.status_code == 200

    def test_filter_by_country(self, api_client):
        provider_1 = ProviderFactory(name='First', provider=None, level=Provider.ProviderLevelChoices.FIRST_LEVEL)
        provider_2 = ProviderFactory(name='Second', provider=None, level=Provider.ProviderLevelChoices.FIRST_LEVEL)
        provider_3 = ProviderFactory(name='Third', provider=None, level=Provider.ProviderLevelChoices.FIRST_LEVEL)
        provider_4 = ProviderFactory(name='Fourth', provider=None, level=Provider.ProviderLevelChoices.FIRST_LEVEL)
        provider_5 = ProviderFactory(name='Fifth', provider=None, level=Provider.ProviderLevelChoices.FIRST_LEVEL)

        ContactFactory(country='Belarus', provider=provider_1)
        ContactFactory(country='Belarus', provider=provider_2)
        ContactFactory(country='Poland', provider=provider_3)
        ContactFactory(country='France', provider=provider_4)
        ContactFactory(country='England', provider=provider_5)

        response = api_client.get('/api/providers/?country=Belarus')

        assert response.status_code == 200
        assert len(response.data) == 2
