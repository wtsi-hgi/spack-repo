# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRecaptchaClient(PythonPackage):
    """Plugin for the legacy reCAPTCHA API, including Mailhide helpers."""

    homepage = "https://pypi.org/project/recaptcha-client/"
    pypi = "recaptcha-client/recaptcha-client-1.0.6.tar.gz"

    import_modules = ["recaptcha.client.captcha"]

    version("1.0.1", sha256="45a3ac063857eea62cf6c8de4897b84114c35172b50a3d0248bc064867b2a917")
    version("1.0.2", sha256="9e629f534ee8d8a8c0fc757d6b5165d2102917ea43dc5c321571135be53ea541")
    version("1.0.3", sha256="5d111575d93892904906e51817a3cb7d7361d2dfd816f2490d1efe5afe5c5e3e")
    version("1.0.4", sha256="95695786a4c19c90d299959bb1f67ee7777a9b9249672c5800d854d36f846690")
    version("1.0.5", sha256="f3801b62f9c1d083164bc0e1e52c847adebd423c5cbb170f2ff40d681ef3a86e")
    version("1.0.6", sha256="28c6853c1d13d365b7dc71a6b05e5ffb56471f70a850de318af50d3d7c0dea2f")

    depends_on("py-setuptools", type="build")

    def patch(self):
        file_path = "recaptcha/client/captcha.py"
        filter_file(
            "import urllib2, urllib",
            (
                "import urllib.parse as urlparse\n"
                "import urllib.request as urlrequest\n\n"
                "try:\n"
                "    unicode\n"
                "except NameError:\n"
                "    unicode = str"
            ),
            file_path,
            string=True,
        )
        filter_file("params = urllib.urlencode ({", "params = urlparse.urlencode ({", file_path, string=True)
        filter_file("request = urllib2.Request", "request = urlrequest.Request", file_path, string=True)
        filter_file("httpresp = urllib2.urlopen (request)", "httpresp = urlrequest.urlopen (request)", file_path, string=True)
        filter_file("            })", "            })\n\n    params = params.encode('utf-8')", file_path, string=True)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import recaptcha.client.captcha")
