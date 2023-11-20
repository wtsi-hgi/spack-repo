# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLimix(PythonPackage):
    """Limix is a flexible and efficient linear mixed model library with interfaces to Python."""

    homepage = "https://github.com/limix/limix"
    pypi = "limix/limix-3.0.4.tar.gz"

    version("3.0.4", sha256="9e32e82c18d66676c1d3c47c045b535f2064dba5bebafcd4036d1e01ef63d98a")

    depends_on("py-pytest-runner@4.4:", type=("build", "run"))
    depends_on("py-appdirs@1.4.3:", type=("build", "run"))
    depends_on("py-asciitree@0.0.3:", type=("build", "run"))
    depends_on("py-bgen-reader@3.0.5:", type=("build", "run"))
    depends_on("py-blessings@1.7:", type=("build", "run"))
    depends_on("py-brent-search@1.7:", type=("build", "run"))
    depends_on("py-click@7.0:", type=("build", "run"))
    depends_on("py-colorama@0.4.1:", type=("build", "run"))
    depends_on("py-dask@2.5.0:+array+dataframe", type=("build", "run"))
    depends_on("py-glimix-core@3.1.8:", type=("build", "run"))
    depends_on("py-h5py@2.9.0:", type=("build", "run"))
    depends_on("py-humanfriendly@2.9.0:", type=("build", "run"))
    depends_on("py-joblib@0.13.2:", type=("build", "run"))
    depends_on("py-limix-plot@0.1.0:", type=("build", "run"))
    depends_on("py-loguru@0.3.1:", type=("build", "run"))
    depends_on("py-matplotlib@3.0.3:", type=("build", "run"))
    depends_on("py-monotonic@1.5:", type=("build", "run"))
    depends_on("py-ndarray-listener@2.0.0:", type=("build", "run"))
    depends_on("py-netcdf4@1.5.0.1:", type=("build", "run"))
    depends_on("py-numba@0.43.1:", type=("build", "run"))
    depends_on("py-numpy-sugar@1.5.0:", type=("build", "run"))
    depends_on("py-numpy@1.17.2:", type=("build", "run"))
    depends_on("py-optimix@3.0.3:", type=("build", "run"))
    depends_on("py-pandas-plink@2.0.1:", type=("build", "run"))
    depends_on("py-pandas@0.24.2:", type=("build", "run"))
    depends_on("py-pytest-doctestplus@0.4.0:", type=("build", "run"))
    depends_on("py-pytest-remfiles@0.0.2:", type=("build", "run"))
    depends_on("py-qtoml@0.2.4:", type=("build", "run"))
    depends_on("py-scikit-learn@0.20.3:", type=("build", "run"))
    depends_on("py-scipy@1.2.1:", type=("build", "run"))
    depends_on("py-seaborn@0.9.0:", type=("build", "run"))
    depends_on("py-setuptools@41.0.0:", type=("build", "run"))
    depends_on("py-statsmodels@0.9.0:", type=("build", "run"))
    depends_on("py-tqdm@4.31.1:", type=("build", "run"))
    depends_on("py-xarray@0.13.0:", type=("build", "run"))
