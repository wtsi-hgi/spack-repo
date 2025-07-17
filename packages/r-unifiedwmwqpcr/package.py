# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnifiedwmwqpcr(RPackage):
    """Unified Wilcoxon-Mann Whitney Test for testing differential expression in qPCR data

    This packages implements the unified Wilcoxon-Mann-Whitney Test for qPCR data. This modified test allows for testing differential expression in qPCR data.
    """

    bioc = "unifiedWMWqPCR"

    version("1.44.0", commit="439a842f878811858b684e8995081ca94717f237")
    version("1.38.0", commit="168af0dcc50592515273b7aa37582db2b67f34ec")

    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-htqpcr", type=("build", "run"))
