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
#     spack install fluidsynth
#
# You can edit this file again by typing:
#
#     spack edit fluidsynth
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Fluidsynth(CMakePackage):
    """FluidSynth is a cross-platform, real-time software synthesizer based on the Soundfont 2 specification."""

    homepage = "https://www.fluidsynth.org/"
    url = "https://github.com/FluidSynth/fluidsynth/archive/refs/tags/v2.3.5.tar.gz"

    license("LGPL v2.1")

    version("2.3.5", sha256="f89e8e983ecfb4a5b4f5d8c2b9157ed18d15ed2e36246fa782f18abaea550e0d")
    version("2.3.4", sha256="1529ef5bc3b9ef3adc2a7964505912f7305103e269e50cc0316f500b22053ac9")
    version("2.3.3", sha256="321f7d3f72206b2522f30a1cb8ad1936fd4533ffc4d29dd335b1953c9fb371e6")
    version("2.3.2", sha256="cd610810f30566e28fb98c36501f00446a06fa6bae3dc562c8cd3868fe1c0fc7")
    version("2.3.1", sha256="d734e4cf488be763cf123e5976f3154f0094815093eecdf71e0e9ae148431883")
    version("2.3.0", sha256="1df5a1afb91acf3b945b7fdb89ac0d99877622161d9b5155533da59113eaaa20")
    version("2.2.9", sha256="bc62494ec2554fdcfc01512a2580f12fc1e1b01ce37a18b370dd7902af7a8159")
    version("2.2.8", sha256="7c29a5cb7a2755c8012d941d1335da7bda957bbb0a86b7c59215d26773bb51fe")
    version("2.2.7", sha256="460d86d8d687f567dc4780890b72538c7ff6b2082080ef2f9359d41670a309cf")
    version("2.2.6", sha256="ca90fe675cacd9a7b442662783c4e7fa0e1fd638b28d64105a4e3fe0f618d20f")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("glib")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
