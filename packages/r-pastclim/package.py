# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPastclim(RPackage):
    """Manipulate Time Series of Palaeoclimate Reconstructions

          Methods to easily extract and manipulate palaeoclimate
    reconstructions for ecological and anthropological analyses, as described
    in Leonardi et al. (2023) <doi:10.1111/ecog.06481>.
    """

    homepage = "https://github.com/EvolEcolGroup/pastclim"
    cran = "pastclim"

    version("2.0.0", md5="c17ec92c8fbe9fb9e95e034da9f2cef8")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-terra@1.7.18:", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-lubridate", type=("build", "run"))
    depends_on("r-ncdf4", type=("build", "run"))
    depends_on("gdal+netcdf", type=("build", "run"))
