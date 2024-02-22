# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbsmapping(RPackage):
	"""Mapping Fisheries Data and Spatial Analysis Tools

	This software has evolved from fisheries research conducted at the
   Pacific Biological Station (PBS) in 'Nanaimo', British Columbia, Canada. It
   extends the R language to include two-dimensional plotting features similar
   to those commonly available in a Geographic Information System (GIS).
   Embedded C code speeds algorithms from computational geometry, such as
   finding polygons that contain specified point events or converting between
   longitude-latitude and Universal Transverse Mercator (UTM) coordinates.
   Additionally, we include 'C++' code developed by Angus Johnson for the
   'Clipper' library, data for a global shoreline, and other data sets in the
   public domain. Under the user's R library directory '.libPaths()',
   specifically in './PBSmapping/doc', a complete user's guide is offered and
   should be consulted to use package functions effectively.
	"""
	
	homepage = "https://github.com/pbs-software/pbs-mapping"
	cran = "PBSmapping" 

	version("2.73.4", md5="468e4e45907dad5372dc6551e5dec0c9")

	depends_on("r@3.5:", type=("build", "run"))
