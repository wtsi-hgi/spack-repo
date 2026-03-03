# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoundshape(RPackage):
	"""Sound Waves Onto Morphometric Data

	Implement a promising, and yet little explored protocol for bioacoustical analysis, the eigensound method by MacLeod, Krieger and Jones (2013) <doi:10.4404/hystrix-24.1-6299>. Eigensound is a multidisciplinary method focused on the direct comparison between stereotyped sounds from different species. 'SoundShape', in turn, provide the tools required for anyone to go from sound waves to Principal Components Analysis, using tools extracted from traditional bioacoustics (i.e. 'tuneR' and 'seewave' packages), geometric morphometrics (i.e. 'geomorph' package) and multivariate analysis (e.g. 'stats' package). For more information, please see Rocha and Romano (2021) and check 'SoundShape' repository on GitHub for news and updates <https://github.com/p-rocha/SoundShape>.
	"""
	
	homepage = "https://github.com/p-rocha/SoundShape"
	cran = "SoundShape" 

	version("1.3.0", md5="fbf9883c7738591d98e7deee45518eb7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-geomorph@3.0.2:", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
