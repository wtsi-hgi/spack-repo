# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-pbcommand
#
# You can edit this file again by typing:
#
#     spack edit py-pbcommand
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPbcommand(PythonPackage):
    """PacBio library for common utils, models, and tools to interface with pbsmrtpipe workflow engine.

    1. Common Models and Schemas
    2. Service client layer to the SMRTLink services
    3. Tool Contract and Resolved Tool Contract interface for integrating with pbsmrtpipe and SMRT Link
    """

    homepage = "https://github.com/PacificBiosciences/pbcommand"

    url = "https://github.com/PacificBiosciences/pbcommand/archive/refs/tags/2.1.1.tar.gz"

    license("PacBio open source license")

    version("2.1.1", sha256="bc6b60c4b08958721eae023afea2b4f9a2ab38db28fd2278e443795825e71014")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-iso8601", type=("build", "run"))
    depends_on("py-avro", type=("build", "run"))
    depends_on("py-pytz", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
