# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqHotspot(RPackage):
    """Targeted sequencing panel design based on mutation hotspots

    seq.hotSPOT provides a resource for designing effective sequencing panels to help improve mutation capture efficacy for ultradeep sequencing projects. Using SNV datasets, this package designs custom panels for any tissue of interest and identify the genomic regions likely to contain the most mutations. Establishing efficient targeted sequencing panels can allow researchers to study mutation burden in tissues at high depth without the economic burden of whole-exome or whole-genome sequencing. This tool was developed to make high-depth sequencing panels to study low-frequency clonal mutations in clinically normal and cancerous tissues.
    """

    homepage = "https://github.com/sydney-grant/seq.hotSPOT"
    bioc = "seq.hotSPOT"

    version("1.8.0", commit="0beecb6750c52066177cae80649d1d8c38ba5f26")
    version("1.2.0", commit="cb30059887db89dcf88739b79876064086e59e82")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-hash", type=("build", "run"))
