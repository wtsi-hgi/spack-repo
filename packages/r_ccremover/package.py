# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcremover(RPackage):
	"""Removes the Cell-Cycle Effect from Single-Cell RNA-Sequencing
Data

	Implements a method for identifying and removing
				the cell-cycle effect from scRNA-Seq data. The description of the 
				method is in Barron M. and Li J. (2016) <doi:10.1038/srep33892>. Identifying and removing 
				the cell-cycle effect from single-cell RNA-Sequencing data. Submitted. 
				Different from previous methods, ccRemover implements a mechanism that
				formally tests whether a component is cell-cycle related or not, and thus
				while it often thoroughly removes the cell-cycle effect, it preserves
				other features/signals of interest in the data.
	"""
	
	cran = "ccRemover" 

	version("1.0.4", md5="7713243bf759b088914a15cddabc2acf")

	depends_on("r@2.10:", type=("build", "run"))
