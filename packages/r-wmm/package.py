# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWmm(RPackage):
	"""World Magnetic Model

	Calculate magnetic field at a given location and time according to 
  the World Magnetic Model (WMM). Both the main field and secular variation 
  components are returned. This functionality is useful for physicists and 
  geophysicists who need orthogonal components from WMM. Currently, this package 
  supports annualized time inputs between 2000 and 2025. If desired, users can
  specify which WMM version to use, e.g., the original WMM2015 release or the 
  recent out-of-cycle WMM2015 release. Methods used to implement WMM, including 
  the Gauss coefficients for each release, are described in the following 
  publications: Chulliat et al (2020) <doi:10.25923/ytk1-yx35>,
  Chulliat et al (2019) <doi:10.25921/xhr3-0t19>, 
  Chulliat et al (2015) <doi:10.7289/V5TB14V7>, 
  Maus et al (2010) <https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/WMM2010_Report.pdf>, 
  McLean et al (2004) <https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/TRWMM_2005.pdf>,
  and Macmillian et al (2000) <https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/wmm2000.pdf>.
	"""
	
	homepage = "https://github.com/wfrierson/wmm"
	cran = "wmm" 

	version("1.1.1", md5="5e94562fd23cae303f102313f536a9e8")

	depends_on("r@2.10:", type=("build", "run"))
