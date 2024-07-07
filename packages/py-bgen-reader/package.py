# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBgenReader(PythonPackage):
    """Bgen is a file format for storing large genetic datasets. It supports both unphased genotypes and phased haplotype data with variable ploidy and number of alleles. It was designed to provides a compact data representation without sacrificing variant access performance."""

    homepage = "https://github.com/limix/bgen-reader-py"
    pypi = "bgen-reader/bgen-reader-4.0.8.tar.gz"

    version("4.0.8", sha256="50414918914b8cd893d0dfa7fef32ee1912ba1802ead37d9502b3d8936d8c68a")

    depends_on("py-appdirs@1.4.3:", type=("build", "run"))
    depends_on("py-cachetools@3.1.1:", type=("build", "run"))
    depends_on("py-cbgen@1.0.1:", type=("build", "run"))
    depends_on("py-dask@2022.10.2:+array+dataframe", type=("build", "run"))
    depends_on("py-numpy@1.17.0:", type=("build", "run"))
    depends_on("py-pandas@1.1.1:", type=("build", "run"))
    depends_on("py-pytest@5.4.1:", type=("build", "run"))
    depends_on("py-requests@1.25.8:", type=("build", "run"))
    depends_on("py-texttable@1.6.2:", type=("build", "run"))
    depends_on("py-tqdm@4.43.0:", type=("build", "run"))
    depends_on("py-xarray@0.16.0:", type=("build", "run"))
