<template>
    <div v-for="city in savedCities" :key="city.id">
        <CityCard :city="city" @click="goToCityView(city)"/>
    </div>
    <p v-if="savedCities.length === 0">Ingen steder lagt til. For å legge til søk i feltet over.</p>
</template>

<script setup>
import {ref} from "vue";
import axios from "axios";
import CityCard from "@/components/CityCard.vue";
import {useRouter} from "vue-router";

const router = useRouter();
const savedCities = ref([])
const goToCityView = (city) => {
    router.push({
        name: "cityView",
        params: {
            state: city.state,
            city: city.city,
        },
        query: {
            id: city.id,
            lat: city.coords.lat,
            lng: city.coords.lng,
        },
    });
}
const getCities = async () => {
    if(localStorage.getItem('savedCities')) {
        savedCities.value = JSON.parse(localStorage.getItem('savedCities'));
    const requests = [];
    savedCities.value.forEach((city) => {
        requests.push(
            axios.get(`https://api.openweathermap.org/data/2.5/weather?lat=${city.coords.lat}&lon=${city.coords.lng}&appid=${import.meta.env.VITE_WEATHER_API_KEY}&units=metric`)
        );
    })
    const weatherData = await Promise.all(requests);
    await new Promise((res) => setTimeout(res, 1000));
    weatherData.forEach((value,index) => {
        savedCities.value[index].weather = value.data;
    })
    }
}
await getCities();
</script>
