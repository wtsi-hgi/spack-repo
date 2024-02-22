# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStandardlastprofile(RPackage):
	"""Data Package for BDEW Standard Load Profiles in Electricity

	Data on standard load profiles from the German Association of 
  Energy and Water Industries (BDEW Bundesverband der Energie- und 
  Wasserwirtschaft e.V.) in a tidy format. The data and methodology are 
  described in VDEW (1999), "Repräsentative VDEW-Lastprofile", 
  <https://www.bdew.de/media/documents/1999_Repraesentative-VDEW-Lastprofile.pdf>.
  The package also offers an interface for generating a standard load profile 
  over a user-defined period. For the algorithm, see VDEW (2000), 
  "Anwendung der Repräsentativen VDEW-Lastprofile step-by-step",
  <https://www.bdew.de/media/documents/2000131_Anwendung-repraesentativen_Lastprofile-Step-by-step.pdf>.
	"""
	
	homepage = "https://github.com/flrd/standardlastprofile"
	cran = "standardlastprofile" 

	version("1.0.0", md5="162e1ece0c9a7ec2ed1270738aa75e62")

	depends_on("r@2.10:", type=("build", "run"))
