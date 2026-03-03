# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextplot(RPackage):
	"""Text Plots

	Visualise complex relations in texts. This is done by providing functionalities for displaying 
    text co-occurrence networks, text correlation networks, dependency relationships as well as text clustering and semantic text 'embeddings'. 
    Feel free to join the effort of providing interesting text visualisations.
	"""
	
	homepage = "https://github.com/bnosac/textplot"
	cran = "textplot" 

	version("0.2.2", md5="46c7a062de7bfb55b5e51c6aded3eca9")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
