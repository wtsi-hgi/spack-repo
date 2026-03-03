# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpendemic(RPackage):
	"""A Glimpse at the Diversity of Peru's Endemic Plants

	Introducing a novel and updated database showcasing Peru's endemic plants. This meticulously compiled and revised botanical collection encompasses a remarkable assemblage of over 7,249 distinct species. The data for this resource was sourced from the work of Govaerts, R., Nic Lughadha, E., Black, N. et al., titled 'The World Checklist of Vascular Plants: A continuously updated resource for exploring global plant diversity', published in Sci Data 8, 215 (2021) <doi:10.1038/s41597-021-00997-6>.
	"""
	
	homepage = "https://github.com/PaulESantos/ppendemic/"
	cran = "ppendemic" 

	version("0.1.7", md5="7b33a2b3ac6ff333d0ccd98c44502e5d")

	depends_on("r@3.5:", type=("build", "run"))
