# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPandasPlink(PythonPackage):
    """Pandas-plink is a Python package for reading PLINK binary file format andrealized relationship matrices (PLINK or GCTA)."""

    homepage = "https://github.com/limix/pandas-plink"
    pypi = "pandas_plink/pandas_plink-2.2.9.tar.gz"

    version("2.2.9", sha256="f5ecacc46c7b92d67968310d14000327333ec1720f35142b091e56da6ef80711")

    depends_on("py-cffi@1.14.3", type=("build", "run"))
    depends_on("py-dask@2.6.0:+array+dataframe", type=("build", "run"))
    depends_on("py-numpy@1.17.2:", type=("build", "run"))
    depends_on("py-pandas@1.1.3:", type=("build", "run"))
    depends_on("py-pytest@5.2.2:", type=("build", "run"))
    depends_on("py-tqdm@4.36.1:", type=("build", "run"))
    depends_on("py-xarray@0.18.2:", type=("build", "run"))
    depends_on("py-zstandard@0.13.0:", type=("build", "run"))
