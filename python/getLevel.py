import xarray as xr

for td in ['IWNoLeith', 'IWAllLeith']:
    todo = '../results/{}/input/spinup.nc'.format(td)
    k = 50
    with xr.open_dataset(todo) as ds:
        print(ds)
        ds = ds.isel(k=k, k_u=k, k_l=k, record=-1)
        ds.to_netcdf('../reduceddata/{}/Level{:04d}.nc'.format(td, k))
