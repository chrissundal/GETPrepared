import { useEffect, useState } from "react";
import axios from "axios";

const useFetch = (url) => {
	const [data, setData] = useState(null);
	const [isPending, setIsPending] = useState(true);

	useEffect(() => {
		const abortController = new AbortController();
		const fetchData = async () => {
			setIsPending(true);
			try {
			const response = await axios.get(url, { signal: abortController.signal })
				if (response.status === 200) {
					setData(response.data);
					setIsPending(false);
				} else {
					throw new Error("Error fetching data");
				}
			} catch (err) {
				if (axios.isCancel(err)) {
					console.log("Fetch request was canceled");
				} else {
					setIsPending(false);
					console.error(err);
				}
			}
		}
		fetchData();
		return () => abortController.abort();
	}, [url]);
	return { data, isPending }
}
export default useFetch;