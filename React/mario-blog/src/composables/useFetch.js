import { useEffect, useState } from "react";
import axios from "axios";

const useFetch = (url) => {
	const [data, setData] = useState(null);
	const [isPending, setIsPending] = useState(true);

	useEffect(() => {
		const abortController = new AbortController();
		setIsPending(true);
		axios.get(url, { signal: abortController.signal })
			.then(response => {
				if (response.status === 200) {
					setData(response.data);
					setIsPending(false);
				}
			})
			.catch(err => {
				if (axios.isCancel(err)) {
					console.log("Fetch request was canceled");
				} else {
					setIsPending(false);
					console.error(err);
				}
			})
		return () => abortController.abort();
	}, [url]);
	return { data, isPending }
}
export default useFetch;