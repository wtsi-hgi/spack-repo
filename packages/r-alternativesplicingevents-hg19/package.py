# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlternativesplicingeventsHg19(RPackage):
    """Alternative splicing event annotation for Human (hg19)

    Data frame containing alternative splicing events. The splicing events were compiled from the annotation files used by the alternative splicing quantification tools MISO, VAST-TOOLS, SUPPA and rMATS.
    """

    homepage = "https://github.com/nuno-agostinho/alternativeSplicingEvents.hg19"
    bioc = "alternativeSplicingEvents.hg19"

    version("1.1.0", commit="2ec71aee8cb767335fd13a29a15332fa3bfe6f10")
    version("1.1.0", commit="2ec71aee8cb767335fd13a29a15332fa3bfe6f10")

    depends_on("r-annotationhub", type=("build", "run"))
