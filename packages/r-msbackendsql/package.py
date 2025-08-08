# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbackendsql(RPackage):
    """SQL-based Mass Spectrometry Data Backend

    SQL-based mass spectrometry (MS) data backend supporting also storange and handling of very large data sets. Objects from this package are supposed to be used with the Spectra Bioconductor package. Through the MsBackendSql with its minimal memory footprint, this package thus provides an alternative MS data representation for very large or remote MS data sets.
    """

    homepage = "https://github.com/RforMassSpectrometry/MsBackendSql"
    bioc = "MsBackendSql"

    version("1.8.0", commit="a307249d468568e8aa9c5702c629e5eef70b05bd")
    version("1.2.0", commit="fff658b9d362e29ace9bc0d40d000288efdcf3b1")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-spectra@1.9.12:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-protgenerics", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-mscoreutils", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-fastmatch", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
