import speedtest

def test_speed():
    servers = []
    threads = None

    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Get the closest servers
    st.get_servers(servers)

    # Run the speed test
    st.get_best_server()
    st.download(threads=threads)
    st.upload(threads=threads)

    # Get the results
    results_dict = st.results.dict()

    # Print the results
    print("Download speed: {:.2f} Mbps".format(results_dict["download"] / 1e6))
    print("Upload speed: {:.2f} Mbps".format(results_dict["upload"] / 1e6))
    print("Ping: {} ms".format(results_dict["ping"]))

if __name__ == "__main__":
    test_speed()
