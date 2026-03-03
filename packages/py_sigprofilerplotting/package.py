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
#     spack install py-sigprofilerplotting
#
# You can edit this file again by typing:
#
#     spack edit py-sigprofilerplotting
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySigprofilerplotting(PythonPackage):
    """SigProfilerPlotting provides a standard tool for displaying all types of mutational signatures as well as all types of mutational patterns in cancer genomes. The tool seamlessly integrates with other SigProfiler tools."""

    homepage = "https://github.com/AlexandrovLab/SigProfilerPlotting"

    url = "https://github.com/AlexandrovLab/SigProfilerPlotting/archive/refs/tags/v1.3.24.tar.gz"

    license("BSD-2-Clause")

    version(
        "1.3.24",
        sha256="807abcc6664c0f59af716d8f1e3c10b6ff06ae46c587e45782ab33e95b2cb5bb",
    )
    version(
        "1.3.23",
        sha256="38c8dee281df23da131da8019c368fd905a9ba4074a7b63f647c049f8866543d",
    )
    version(
        "1.3.22",
        sha256="5e701694b315880390ccdcbd8004ab44b37ffabccf8206b2d964e36282b3056e",
    )
    version(
        "1.3.21",
        sha256="d8e2ca065c14022cf8c84e505f80775db1b39aeb72fa2c06354bae59673b884a",
    )
    version(
        "1.3.20",
        sha256="47da37a2a3fd56120f6e0efa024254c8ccf1442e365cbc22006ca4fdd904edbb",
    )
    version(
        "1.3.19",
        sha256="f16e24258568a0651b47234d17178b7fb9be1ede3a735068e15c0554695cdf8e",
    )
    version(
        "1.3.18",
        sha256="0dc0b7cc462663e201fa1760e5bea3f2d2803e7c127467b5b12adc1017784fb8",
    )
    version(
        "1.3.17",
        sha256="fb337a3fdc8714ec59b2142ade9ed1fde4f282d712e7ae0eefd960f5bd5aa83b",
    )
    version(
        "1.3", sha256="8f89290f7f7d1c3c87d2785fef906596f72b41cbfca3bd4bcdab1c59f46be63b"
    )
    version(
        "1.2", sha256="2ed296107a88d07c4ab0819f82be8713cf24c4554823695b4928c28035c5b9d1"
    )

    depends_on("py-setuptools", type="build")

    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
