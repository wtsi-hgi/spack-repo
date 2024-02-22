# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProvviz(RPackage):
	"""Provenance Visualizer

	Displays provenance graphically for provenance collected by the 'rdt' or
  'rdtLite' packages, or other tools providing compatible PROV JSON output. The exact 
  format of the JSON created by 'rdt' and 'rdtLite' is described in 
  <https://github.com/End-to-end-provenance/ExtendedProvJson>.  More information about
  rdtLite and associated tools is available at <https://github.com/End-to-end-provenance/> 
  and Barbara Lerner, Emery Boose, and Luis Perez (2018), Using Introspection to Collect 
  Provenance in R, Informatics, <doi: 10.3390/informatics5010012>.
	"""
	
	homepage = "https://github.com/ProvTools/provViz"
	cran = "provViz" 

	version("1.0.9", md5="c48cff5b6eff1f03b71bbdc4f0c6800f")

	depends_on("r@3.5:", type=("build", "run"))
