# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprdesignr(RPackage):
	"""Guide Sequence Design for CRISPR/Cas9

	Designs guide sequences for CRISPR/Cas9 genome editing and 
    provides information on sequence features pertinent to guide 
    efficiency. Sequence features include annotated off-target 
    predictions in a user-selected genome and a predicted efficiency 
    score based on the model described in Doench et al. (2016) 
    <doi:10.1038/nbt.3437>. Users are able to import additional genomes 
    and genome annotation files to use when searching and annotating 
    off-target hits. All guide sequences and off-target data can be 
    generated through the 'R' console with sgRNA_Design() or through 
    'crispRdesignR's' user interface with crispRdesignRUI(). CRISPR 
    (Clustered Regularly Interspaced Short Palindromic Repeats) and the 
    associated protein Cas9 refer to a technique used in genome editing.
	"""
	
	homepage = "<https://github.com/dylanbeeber/crispRdesignR>"
	cran = "crispRdesignR" 

	version("1.1.7", md5="aec8f744489761454537f0de33b57ec7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-vtreat", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
