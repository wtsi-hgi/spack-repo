# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoggit(RPackage):
	"""Modern Logging for the R Ecosystem

	
    An effortless 'ndjson' (newline-delimited 'JSON') logger, with two primary
    log-writing interfaces. It provides a set of wrappings for base R's
    message(), warning(), and stop() functions that maintain identical
    functionality, but also log the handler message to an 'ndjson' log file.
    'loggit' also exports its internal 'loggit()' function for powerful and
    configurable custom logging. No change in existing code is necessary to use
    this package, and should only require additions to fully leverage the power
    of the logging system. 'loggit' also provides a log reader for reading an
    'ndjson' log file into a data frame, log rotation, and live echo of the
    'ndjson' log messages to terminal 'stdout' for log capture by external
    systems (like containers). 'loggit' is ideal for Shiny apps, data pipelines,
    modeling work flows, and more. Please see the vignettes for detailed example
    use cases.
	"""
	
	homepage = "https://github.com/ryapric/loggit"
	cran = "loggit" 

	version("2.1.1", md5="37f1814adcafffabe20808a4d5586d0f")

	depends_on("r@3.4:", type=("build", "run"))
