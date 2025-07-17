# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaddV16Hg38(RPackage):
    """CADD v1.6 Pathogenicity Scores AnnotationHub Resource Metadata for hg38

    Store University of Washington CADD v1.6 hg38 pathogenicity scores AnnotationHub Resource Metadata. Provide provenance and citation information for University of Washington CADD v1.6 hg38 pathogenicity score AnnotationHub resources. Illustrate in a vignette how to access those resources.
    """

    bioc = "cadd.v1.6.hg38"

    version("3.18.1", commit="73d90290e5bb58c3ccd3a2ff336893331d2b8943")
    version("3.18.1", commit="73d90290e5bb58c3ccd3a2ff336893331d2b8943")

    depends_on("r-genomicscores", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
