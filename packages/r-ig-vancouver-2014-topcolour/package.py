# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgVancouver2014Topcolour(RPackage):
	"""Instagram 2014 Vancouver Top Colour Dataset

	A dataset of the top colours of photos from Instagram 
 taken in 2014 in the city of Vancouver, British Columbia, Canada.
 It consists of: top colour and counts data. This data was
 obtained using the Instagram API. Instagram is a web photo 
 sharing service. It can be found at: <https://instagram.com>.
 The Instagram API is documented at: <https://instagram.com/developer/>. 
	"""
	
	cran = "ig.vancouver.2014.topcolour" 

	version("0.1.2.0", md5="88cb342589f915f197357580666d66ad")

	depends_on("r@2.10:", type=("build", "run"))
