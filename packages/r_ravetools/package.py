# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRavetools(RPackage):
	"""Signal and Image Processing Toolbox for Analyzing Intracranial
'Electroencephalography' Data

	Implemented fast and memory-efficient 'Notch'-filter, 
    'Welch-periodogram', discrete wavelet transform algorithm for hours of 
    high-resolution signals, fast 3D convolution, and image alignment;
    providing fundamental toolbox for 'iEEG' pipelines. 
    Documentation and examples about 'RAVE' project are provided at 
    <https://openwetware.org/wiki/RAVE>, and the paper by John F. Magnotti, 
    Zhengjia Wang, Michael S. Beauchamp (2020) 
    <doi:10.1016/j.neuroimage.2020.117341>; see 'citation("ravetools")' for 
    details.
	"""
	
	homepage = "https://dipterix.org/ravetools/"
	cran = "ravetools" 

	version("0.1.3", md5="ea4bc3f0e5bb837679697bd529fdaa3c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-filearray@0.1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-waveslim@1.8.2:", type=("build", "run"))
	depends_on("r-signal@0.7.7:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-digest@0.6.29:", type=("build", "run"))
	depends_on("r-rniftyreg@2.7.1:", type=("build", "run"))
	depends_on("r-rvcg@0.22.1:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
	depends_on("pkg-config", type=("build", "link", "run"))

	def patch(self):
		filter_file("ac_unique_file=\"ravetools\"", "ac_unique_file=\"spack-src\"", "configure", string=True)
