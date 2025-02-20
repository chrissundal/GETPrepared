<template>
    <div v-if="weatherData">
        <div class="flex flex-col flex-1 items-center">
            <div v-if="route.query.preview" class="text-white p-4 bg-weather-secondary w-full text-center">
                <p>Du ser nå på byen, klikk på "+" ikonet for å begynne å følge byen</p>
            </div>
        </div>
        <div class="flex flex-col items-center text-white py-12">
            <h1 class="text-4xl mb-2">{{route.params.city}}</h1>
            <p class="text-sm mb-12">
                {{new Date().toLocaleString()}}
            </p>
            <p class="text-8xl mb-8">
                {{Math.round(weatherData.list[0].main.temp)}}&deg
            </p>
            <p>Føles som: {{Math.round(weatherData.list[0].main.feels_like)}}&deg</p>
            <p class="capitalize">
                {{weatherData.list[0].weather[0].description}}
            </p>
            <i :class="`owi owi-${weatherData.list[0].weather[0].icon}`"></i>
        </div>
        <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
            <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Dato</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Klokkeslett</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"></th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Beskrivelse</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Temperatur (&deg;C)</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Føles som (&deg;C)</th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Vind hastighet (m/s)</th>
            </tr>
            </thead>
            <tbody class=" divide-y divide-gray-200 text-white">
            <tr v-for="day in filteredWeatherData" :key="day.dt">
                <td class="px-6 py-4 whitespace-nowrap">{{ new Date(day.dt_txt).toLocaleDateString().slice(0,2) }}</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ new Date(day.dt_txt).toLocaleTimeString().slice(0, 5) }}</td>
                <td class="px-6 py-4 whitespace-nowrap"><i :class="`owi owi-${day.weather[0].icon}`"></i></td>
                <td class="px-6 py-4 whitespace-nowrap">{{ day.weather[0].description }}</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ Math.round(day.main.temp) }}&deg;</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ Math.round(day.main.feels_like) }}&deg;</td>
                <td class="px-6 py-4 whitespace-nowrap">{{ day.wind.speed }} m/s</td>
            </tr>
            </tbody>
        </table>
        <div v-if="!route.query.preview" class="flex justify-center item-center gap-2 py-12 text-white cursor-pointer duration-150 hover:text-red-500" @click="removeCity">
            <i class="fa-solid fa-trash"></i>
            <p>Fjern by</p>
        </div>
    </div>
    <div v-else>
        <CityCardSkeleton />
    </div>

</template>

<script setup>
import axios from "axios";
import {useRoute, useRouter} from "vue-router";
import {computed, onMounted, ref} from "vue";
import '@/assets/open-weather-icons.css';
import CityCardSkeleton from "@/components/CityCardSkeleton.vue";
const route = useRoute();
const router = useRouter();
const weatherData = ref(null);
const getWeatherData = async () => {
    try {
        let response = await axios.get(`https://api.openweathermap.org/data/2.5/forecast?lat=${route.query.lat}&lon=${route.query.lng}&units=metric&appid=${import.meta.env.VITE_WEATHER_API_KEY}&lang=no`);
        await new Promise((res) => setTimeout(res, 1000));
        weatherData.value = response.data;
    } catch (err) {
        console.error(err);
    }
}
Date.prototype.addDays = function(days) {
    const date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
};

const filteredWeatherData = computed(() => {
    const now = new Date();
    const threeDaysFromNow = now.addDays(2);

    return weatherData.value.list.filter(day => {
        const dayDate = new Date(day.dt_txt);
        return dayDate >= now && dayDate <= threeDaysFromNow;
    });
});
const removeCity = () => {
    const cities = JSON.parse(localStorage.getItem("savedCities"));
    const updatedCities = cities.filter((city) => city.id !== route.query.id);
    localStorage.setItem("savedCities", JSON.stringify(updatedCities));
    router.push({name: "home"});
}
onMounted(async () => {
await getWeatherData();

})
</script>
