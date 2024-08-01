# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Gstreamer(MesonPackage):
    """GStreamer: a flexible, fast and multiplatform multimedia framework"""

    homepage = "https://gstreamer.freedesktop.org/"
    url = "https://github.com/GStreamer/gstreamer/archive/refs/tags/1.24.6.tar.gz"

    version("1.24.6", sha256="dde1acbb57bc61d095048985e24bb7eb6cfe614a28a19df5986a0232d2d84f54")

    depends_on("python@3.8:")
    depends_on("gettext")
    depends_on("zlib")
    depends_on("libffi")
    depends_on("glib")
    depends_on("flex")
    depends_on("bison")

