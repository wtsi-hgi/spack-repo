# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtm(RPackage):
	"""Analyses of Protein Post-Translational Modifications

	Contains utilities for the analysis of post-translational modifications (PTMs) in proteins, 
    with particular emphasis on the sulfoxidation of methionine residues. Features include the ability to download, 
    filter and analyze data from the sulfoxidation database 'MetOSite', and integrate data from other main PTMs 
    (other databases). Utilities to search and characterize S-aromatic motifs in proteins are also provided. 
    In addition, functions to analyze sequence environments around modifiable residues in proteins can be found. 
    For instance, 'ptm' allows to search for amino acids either overrepresented or avoided around the modifiable 
    residues from the proteins of interest. Functions tailored to test statistical hypothesis related to
    these differential sequence environments are also implemented. A number of utilities to assess the effect
    of the modification/mutation of a given residue on the protein stability, have also been included in this package.
    Further and detailed information regarding the methods in this package can be found in (Aledo (2020) <https://metositeptm.com>).
	"""
	
	homepage = "https://bitbucket.org/jcaledo/ptm"
	cran = "ptm" 

	version("0.2.6", md5="ea4e21169ee82971e98e4f400f7614f6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bio3d@2.3.4:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-muscle", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
