# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHttpx(PythonPackage):
    """Fully featured sync and async HTTP client with HTTP/1.1 and HTTP/2 support."""

    homepage = "https://github.com/encode/httpx"
    pypi = "httpx/httpx-0.28.1.tar.gz"

    license("BSD-3-Clause")

    version("0.28.1", sha256="75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc")
    version("0.28.0", sha256="0858d3bab51ba7e386637f22a61d8ccddaeec5f3fe4209da3a6168dbb91573e0")
    version("0.27.2", sha256="f7c2be1d2f3c3c3160d441802406b206c2b76f5947b11115e6df10c6c65e66c2")
    version("0.27.0", sha256="a0cb88a46f32dc874e04ee956e4c2764aba2aa228f650b06788ba6bda2962ab5")

    variant("http2", default=False, description="Enable HTTP/2 dependencies")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-fancy-pypi-readme", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-certifi")
        depends_on("py-httpcore@1:1", when="@0.27:")
        depends_on("py-idna@2.8:")
        depends_on("py-anyio@3:", when="@0.27:")
        depends_on("py-sniffio@1:", when="@0.27:0.27.999")

    depends_on("py-h2@3:4", when="+http2", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import httpx; print(httpx.__version__)")
