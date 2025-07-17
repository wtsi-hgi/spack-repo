# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompounddb(RPackage):
    """Creating and Using (Chemical) Compound Annotation Databases

    CompoundDb provides functionality to create and use (chemical) compound annotation databases from a variety of different sources such as LipidMaps, HMDB, ChEBI or MassBank. The database format allows to store in addition MS/MS spectra along with compound information. The package provides also a backend for Bioconductor's Spectra package and allows thus to match experimetal MS/MS spectra against MS/MS spectra in the database. Databases can be stored in SQLite format and are thus portable.
    """

    homepage = "https://github.com/RforMassSpectrometry/CompoundDb"
    bioc = "CompoundDb"

    version("1.12.1", commit="7fffee6fbfe7cffcd63748ac8b693d56c4cbf5ac")
    version("1.6.0", commit="288e0ba28d25f24a8eafdbe2370765babb2be59c")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-annotationfilter", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-chemminer", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-dbplyr", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-protgenerics", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-spectra@1.9.12:", type=("build", "run"))
    depends_on("r-mscoreutils", type=("build", "run"))
    depends_on("r-metabocoreutils", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
