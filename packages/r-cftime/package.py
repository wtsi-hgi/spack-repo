# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCftime(RPackage):
	"""Using CF-Compliant Calendars with Climate Projection Data

	Support for all calendars as specified in the Climate and Forecast 
    (CF) Metadata Conventions for climate and forecasting data. The CF Metadata 
    Conventions is widely used for distributing files with climate observations 
    or projections, including the Coupled Model Intercomparison Project (CMIP) 
    data used by climate change scientists and the Intergovernmental Panel on
    Climate Change (IPCC). This package specifically allows the user to work 
    with any of the CF-compliant calendars (many of which are not compliant with 
    POSIXt). The CF time coordinate is formally defined in the CF Metadata 
    Conventions document available at <https://cfconventions.org/Data/cf-conventions/cf-conventions-1.10/cf-conventions.html#time-coordinate>.
	"""
	
	homepage = "https://github.com/pvanlaake/CFtime"
	cran = "CFtime" 

	version("1.2.0", md5="b1a54ebaaa86b2757c85f6f3fcaddfee")

