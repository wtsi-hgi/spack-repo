# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsd(RPackage):
	"""Graph Signal Decomposition

	Graph signals residing on the vertices of a graph have recently gained prominence in research in various fields. Many methodologies have been proposed to analyze graph signals by adapting classical signal processing tools. Recently, several notable graph signal decomposition methods have been proposed, which include graph Fourier decomposition based on graph Fourier transform, graph empirical mode decomposition, and statistical graph empirical mode decomposition. This package efficiently implements multiscale analysis applicable to various fields, and offers an effective tool for visualizing and decomposing graph signals. For the detailed methodology, see Ortega et al. (2018) <doi:10.1109/JPROC.2018.2820126>, Shuman et al. (2013) <doi:10.1109/MSP.2012.2235192>, Tremblay et al. (2014) <https://www.eurasip.org/Proceedings/Eusipco/Eusipco2014/HTML/papers/1569922141.pdf>, and Cho et al. (2024) "Statistical graph empirical mode decomposition by graph denoising and boundary treatment".
	"""
	
	cran = "GSD" 

	version("1.0.0", md5="2dee95b432929de45b9ea356a40bc9db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ebayesthresh", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
