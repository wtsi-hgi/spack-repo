# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChannelattributionapp(RPackage):
	"""Shiny Web Application for the Multichannel Attribution Problem

	Shiny Web Application for the Multichannel Attribution Problem. It is a user-friendly graphical interface for package 'ChannelAttribution'.
	"""
	
	homepage = "http://www.channelattribution.net"
	cran = "ChannelAttributionApp" 

	version("1.3", md5="99b51a8c2d8af0ce022cf605384217e4")

	depends_on("r-channelattribution", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
