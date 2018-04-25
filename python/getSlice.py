import xarray as xr

for td in [ 'IWNoLeithHR']:
    todo = '../results/{}/input/spinup.nc'.format(td)

    with xr.open_dataset(todo) as ds:
        print(ds)
        ds = ds.isel(j=1280, j_g=1280, record=0)
        ds.to_netcdf('../reduceddata/{}/AllSlice.nc'.format(td))
