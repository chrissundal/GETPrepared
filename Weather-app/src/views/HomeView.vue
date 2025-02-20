<template>
    <main class="container text-white">
        <div class="pt-4 mb-8 relative">
            <input type="text" placeholder="Søk etter by" v-model="searchQuery" @input="getSearchResult" class="py-2 px-1 w-full bg-transparent border-b focus:border-weather-secondary focus:outline-none focus:shadow-[0px_1px_0_0_#004E71]">
            <ul class="absolute bg-weather-secondary text-white w-full shadow-md py-2 px-1 top-[66px]" v-if="mapboxSearchResults">
                <p v-if="searchError">Beklager det skjedde en feil</p>
                <p v-if="!searchError && mapboxSearchResults.length === 0">Ingen resultat funnet</p>
                <template v-else>
                    <li v-for="result in mapboxSearchResults" :key="result.id" class="py-2 cursor-pointer" @click="previewCity(result)">
                        {{result.properties.name}} - {{result.properties.place_formatted}}
                    </li>
                </template>
            </ul>
        </div>
        <div class="flex flex-col gap-4">
            <Suspense>
                <CityList />
                <template #fallback>
                    <CityCardSkeleton />
                </template>
            </Suspense>
        </div>
    </main>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import {useRouter} from "vue-router";
import CityList from "@/components/CityList.vue";
import CityCardSkeleton from "@/components/CityCardSkeleton.vue";
const searchQuery = ref('');
const queryTimeout = ref(null);

const mapboxSearchResults = ref(null);
const searchError = ref(null);
const router = useRouter()

const previewCity = (result) => {
    let city = result.properties.name;
    let state;
    if (result.properties.feature_type == "region") {
        state = result.properties.name;
    }
    else {
        state = result.properties.context.region.name;
    }
    router.push({
        name: "cityView",
        params: {
            state: state,
            city: city,
        },
        query: {
            lat: result.properties.coordinates.latitude,
            lng: result.properties.coordinates.longitude,
            preview: true,
        },
    });
}
const getSearchResult = () => {
    searchError.value = false;
    clearTimeout(queryTimeout.value);
    queryTimeout.value = setTimeout(async () => {
        if (searchQuery.value !== '') {
            try {
                const result = await axios.get(`/api/search/searchbox/v1/forward?q=${searchQuery.value}&access_token=${import.meta.env.VITE_MAPBOX_API_KEY}&types=place`);
                mapboxSearchResults.value = result.data.features;
            } catch {
                searchError.value = true;
            }
            return;
        }
        mapboxSearchResults.value = null;
    }, 300);
};
</script>




