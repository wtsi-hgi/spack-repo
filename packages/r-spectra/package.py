# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectra(RPackage):
    """Spectra Infrastructure for Mass Spectrometry Data

    The Spectra package defines an efficient infrastructure for storing and handling mass spectrometry spectra and functionality to subset, process, visualize and compare spectra data. It provides different implementations (backends) to store mass spectrometry data. These comprise backends tuned for fast data access and processing and backends for very large data sets ensuring a small memory footprint.
    """

    homepage = "https://github.com/RforMassSpectrometry/Spectra"
    bioc = "Spectra"

    version("1.18.2", commit="4d6a810f0236b47b528e2e6d784fded9082d24bf")
    version("1.12.0", commit="f0abdfab5e4742026a1b3f6c91d49fe3717ee546")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-protgenerics@1.33.1:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-mscoreutils@1.7.5:", type=("build", "run"))
    depends_on("r-fs", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-metabocoreutils", type=("build", "run"))
