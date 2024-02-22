# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrometheetools(RPackage):
	"""PROMETHEE and GLNF for Ranking and Sorting Problems

	PROMETHEE (Preference Ranking Organisation METHod for Enrichment of
    Evaluations) based method assesses alternatives to obtain partial and complete
    rankings. The package also provides the GLNF (Global Local Net Flow) sorting
    algorithm to classify alternatives into ordered categories, as well as an index
    function to measure the classification quality. Barrera, F., Segura, M., &
    Maroto, C. (2023) <doi:10.1111/itor.13288>. Brans, J.P.; De Smet, Y., (2016) 
    <doi:10.1007/978-1-4939-3094-4_6>.
	"""
	
	homepage = "https://github.com/ifelipebj/PrometheeTools"
	cran = "PrometheeTools" 

	version("0.1.0", md5="5a35e60a0005bad3f7fe2b8fa06c265c")

	depends_on("r-ggplot2", type=("build", "run"))
