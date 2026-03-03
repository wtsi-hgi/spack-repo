# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyclust(RPackage):
	"""Phylogenetic Clustering (Phyloclustering)

	Phylogenetic clustering (phyloclustering) is an evolutionary
        Continuous Time Markov Chain model-based approach to identify
        population structure from molecular data without assuming
        linkage equilibrium. The package phyclust (Chen 2011) provides a
        convenient implementation of phyloclustering for DNA and SNP data,
        capable of clustering individuals into subpopulations and identifying
        molecular sequences representative of those subpopulations. It is
        designed in C for performance, interfaced with R for visualization,
        and incorporates other popular open source programs including
        ms (Hudson 2002) <doi:10.1093/bioinformatics/18.2.337>,
        seq-gen (Rambaut and Grassly 1997)
        <doi:10.1093/bioinformatics/13.3.235>,
        Hap-Clustering (Tzeng 2005) <doi:10.1002/gepi.20063> and
        PAML baseml (Yang 1997, 2007) <doi:10.1093/bioinformatics/13.5.555>,
        <doi:10.1093/molbev/msm088>,
        for simulating data, additional analyses, and searching the best tree.
        See the phyclust website for more information, documentations and
        examples.
	"""
	
	homepage = "https://snoweye.github.io/phyclust/"
	cran = "phyclust" 

	version("0.1-34", md5="7053b989522f8609b9879690c4eb532d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
