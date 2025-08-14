# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationhubdata(RPackage):
    """Transform public data resources into Bioconductor Data Structures

    These recipes convert a wide variety and a growing number of public bioinformatic data sets into easily-used standard Bioconductor data structures.
    """

    bioc = "AnnotationHubData"

    version("1.38.0", commit="3970916e0dc8a818b4b3956e3e2ced4650212c71")
    version("1.32.1", commit="938caa2d7b93013985938adfa63d896985fba8ba")

    depends_on("r@3.2.2:", type=("build", "run"))
    depends_on("r-s4vectors@0.7.21:", type=("build", "run"))
    depends_on("r-iranges@2.3.23:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-annotationhub@2.15.15:", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-biocviews", type=("build", "run"))
    depends_on("r-bioccheck", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-genomeinfodb@1.15.4:", type=("build", "run"))
    depends_on("r-organismdbi", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-annotationforge", type=("build", "run"))
    depends_on("r-futile-logger@1.3:", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))

    def install(self, spec, prefix):
        """Custom install to avoid getcwd/setwd failures.

        Some Bioconductor installs attempt to return to the original working
        directory after staged installation. When the build is run from inside
        a directory that gets removed during the process, R can error with
        'getcwd() failed' / 'cannot change working directory'. To avoid this,
        run R CMD INSTALL from the stable stage directory and skip test-load.
        """
        library_path = join_path(prefix, "rlib", "R", "library")
        args = [
            "--vanilla",
            "CMD",
            "INSTALL",
            "--no-test-load",
            f"--library={library_path}",
            self.stage.source_path,
        ]
        R = Executable("R")
        with working_dir(self.stage.path):
            R(*args)
