# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhipdata(RPackage):
    """Container for PhIP-Seq Experiments

    PhIPData defines an S4 class for phage-immunoprecipitation sequencing (PhIP-seq) experiments. Buliding upon the RangedSummarizedExperiment class, PhIPData enables users to coordinate metadata with experimental data in analyses. Additionally, PhIPData provides specialized methods to subset and identify beads-only samples, subset objects using virus aliases, and use existing peptide libraries to populate object parameters.
    """

    bioc = "PhIPData"

    version("1.16.1", commit="c2bad37b5341ada725c79d7bc707c3b8266bb035")
    version("1.10.0", commit="463fdc6461af0f0f3dd7a6080d3ef0c628b3ca27")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.3.81:", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
