# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgspectra(RPackage):
	"""Extensions to 'ggplot2' for Radiation Spectra

	Additional annotations, stats, geoms and scales for plotting 
    "light" spectra with 'ggplot2', together with specializations of ggplot()
    and autoplot() methods for spectral data and waveband definitions
    stored in objects of classes defined in package 'photobiology'. Part of the 
    'r4photobiology' suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://docs.r4photobiology.info/ggspectra/"
	cran = "ggspectra" 

	version("0.3.12", md5="4a5d13fe6a4fa0102cc783112c61357f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-photobiology@0.10.16:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-photobiologywavebands@0.5.1:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-ggrepel@0.9.2:", type=("build", "run"))
	depends_on("r-lubridate@1.9:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-tibble@3.1.5:", type=("build", "run"))
