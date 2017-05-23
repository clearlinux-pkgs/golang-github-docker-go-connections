#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-docker-go-connections
Version  : 5b7154ba2efe13ff86ae8830a9e7cb120b080d6e
Release  : 5
URL      : https://github.com/docker/go-connections/archive/5b7154ba2efe13ff86ae8830a9e7cb120b080d6e.tar.gz
Source0  : https://github.com/docker/go-connections/archive/5b7154ba2efe13ff86ae8830a9e7cb120b080d6e.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go

%description
[![GoDoc](https://godoc.org/github.com/docker/go-connections?status.svg)](https://godoc.org/github.com/docker/go-connections)

%prep
%setup -q -n go-connections-5b7154ba2efe13ff86ae8830a9e7cb120b080d6e

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/docker/go-connections"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/docker/go-connections

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/docker/go-connections/doc.go
/usr/lib/golang/src/github.com/docker/go-connections/nat/nat.go
/usr/lib/golang/src/github.com/docker/go-connections/nat/nat_test.go
/usr/lib/golang/src/github.com/docker/go-connections/nat/parse.go
/usr/lib/golang/src/github.com/docker/go-connections/nat/parse_test.go
/usr/lib/golang/src/github.com/docker/go-connections/nat/sort.go
/usr/lib/golang/src/github.com/docker/go-connections/nat/sort_test.go
/usr/lib/golang/src/github.com/docker/go-connections/proxy/network_proxy_test.go
/usr/lib/golang/src/github.com/docker/go-connections/proxy/proxy.go
/usr/lib/golang/src/github.com/docker/go-connections/proxy/stub_proxy.go
/usr/lib/golang/src/github.com/docker/go-connections/proxy/tcp_proxy.go
/usr/lib/golang/src/github.com/docker/go-connections/proxy/udp_proxy.go
/usr/lib/golang/src/github.com/docker/go-connections/sockets/inmem_socket.go
/usr/lib/golang/src/github.com/docker/go-connections/sockets/inmem_socket_test.go
/usr/lib/golang/src/github.com/docker/go-connections/sockets/proxy.go
/usr/lib/golang/src/github.com/docker/go-connections/sockets/sockets.go
/usr/lib/golang/src/github.com/docker/go-connections/sockets/sockets_unix.go
/usr/lib/golang/src/github.com/docker/go-connections/sockets/sockets_windows.go
/usr/lib/golang/src/github.com/docker/go-connections/sockets/tcp_socket.go
/usr/lib/golang/src/github.com/docker/go-connections/sockets/unix_socket.go
/usr/lib/golang/src/github.com/docker/go-connections/tlsconfig/config.go
/usr/lib/golang/src/github.com/docker/go-connections/tlsconfig/config_client_ciphers.go
/usr/lib/golang/src/github.com/docker/go-connections/tlsconfig/config_legacy_client_ciphers.go
/usr/lib/golang/src/github.com/docker/go-connections/tlsconfig/config_test.go
