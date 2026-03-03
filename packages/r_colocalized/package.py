# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColocalized(RPackage):
	"""Clusters of Colocalized Sequences

	Also abbreviates to "CCSeq". Finds clusters of colocalized sequences in .bed annotation files
    up to a specified cut-off distance. Two sequences are colocalized if they
    are within the cut-off distance of each other, and clusters are sets of
    sequences where each sequence is colocalized to at least one other sequence
    in the cluster. For a set of .bed annotation tables provided in a list 
    along with a cut-off distance, the program will output a file containing
    the locations of each cluster. Annotated .bed files are from 
    the 'pwmscan' application at <https://ccg.epfl.ch/pwmtools/pwmscan.php>. 
    Personal machines might crash or take excessively long depending 
    on the number of annotated sequences in each file and whether chromsearch() 
    or gensearch() is used.
	"""
	
	cran = "colocalized" 

	version("0.2.0", md5="6a932d1dcb8104bab2f19a5a0bcb9bbf")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
