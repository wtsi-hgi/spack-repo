# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpmnvisualizationr(RPackage):
	"""Visualize Process Execution Data on 'BPMN' Diagrams

	To visualize the execution data of the processes on 'BPMN' (Business Process Model and Notation) diagrams, using overlays, style customization and interactions, with the 'bpmn-visualization' 'TypeScript' library.
	"""
	
	homepage = "https://process-analytics.github.io/bpmn-visualization-R/"
	cran = "bpmnVisualizationR" 

	version("0.5.0", md5="2c76e55a48d03b5f8d996759c9685e36")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
