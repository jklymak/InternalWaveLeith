import xarray as xr

for td in ['TestIWNoLeith']:
    todo = '../results/{}/input/spinup.nc'.format(td)

    with xr.open_dataset(todo) as ds:
        print(ds)
        ds = ds.isel(j=128, j_g=128, record=0)
        ds.to_netcdf('../reduceddata/{}/AllSlice.nc'.format(td))
