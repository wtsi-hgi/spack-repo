# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoregnet(RPackage):
    """CoRegNet : reconstruction and integrated analysis of co-regulatory networks

    This package provides methods to identify active transcriptional programs. Methods and classes are provided to import or infer large scale co-regulatory network from transcriptomic data. The specificity of the encoded networks is to model Transcription Factor cooperation. External regulation evidences (TFBS, ChIP,...) can be integrated to assess the inferred network and refine it if necessary. Transcriptional activity of the regulators in the network can be estimated using an measure of their influence in a given sample. Finally, an interactive UI can be used to navigate through the network of cooperative regulators and to visualize their activity in a specific sample or subgroup sample. The proposed visualization tool can be used to integrate gene expression, transcriptional activity, copy number status, sample classification and a transcriptional network including co-regulation information.
    """

    bioc = "CoRegNet"

    version("1.40.0", commit="93ca417b50fb0c077ab0d9f5c537a39598aa7eaf")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-arules", type=("build", "run"))
