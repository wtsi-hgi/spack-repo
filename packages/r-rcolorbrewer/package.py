# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RRcolorbrewer(RPackage):
    """Provides color schemes for maps (and other graphics) designed by Cynthia Brewer as described at http://colorbrewer2.org."""

    cran = "RColorBrewer"

    version("1.1-3", sha256="4f42f5423c45688b39f492c7892d93f37b4541831c8ffb140364d2bd89031ac0")
    version("1.1-2", sha256="f3e9781e84e114b7a88eb099825936cc5ae7276bbba5af94d35adb1b3ea2ccdd")
    version("1.0-5", sha256="5ac1c44c1a53f9521134e7ed7c148c72e49271cbd229c5263d2d7fd91c8b8e78")
    version("1.0-4", sha256="4ca3d3fecd540653e515c5759033cc2ad4f93bcb6290a64e7ac2b92befa783d9")
    version("1.0-2", sha256="9effdea3de2e9a4b594c1eef0eefea326dcc4f8a1831aa3d2618c4e08c4aa5bd")
    version("1.0-1", sha256="d7c557122ea6c1adb548f36180c5913e81993c69717490b55e8bb44bfbba8fa7")
    version("0.2-3", sha256="a897a1cc11ecd6768f576463d9a37a9baf011201f485c6d9768e6601815c3b0c")
    version("0.2-2", sha256="630ad62bb9130983261cef233ddfb3fccb48248fa08dcf967553c3755f04341a")
    version("0.2-1", sha256="00379c71f5afa43a9a68f597ee722d8abaf5372fdb6b34ed8372c6717a0ffc41")
    version("0.1-4", sha256="a3f0c1f9a83d0f58f50f7ac6bf430c68da49a0e6b0fde85b4e3503a9ef4f3aa5")
    version("0.1-3", sha256="89239ff01bb41f91ef8ea955f47479509718ca0d7bc7def2c096760e6a57bc55")
    version("0.1-2", sha256="17c6e79c3b88727619581192e2c06fcde2b64ba0a9d1030b9ae588f34a88e397")
    version("0.1-1", sha256="1fe67bc758323b265a6913e47ef2c5729c5fb017ab45b860f55a284fefe7c0ac")
