require 'capistrano'

# config valid for current version and patch releases of Capistrano
lock "~> 3.16.0"

set :application, 'crucible'
set :repo_url, "git@github.com:omarowns/#{fetch :application}.git"
set :branch, 'main'
set :user, 'pi'
set :deploy_to, "/home/#{fetch :user}/#{fetch :application}"

# Default value for :format is :airbrussh.
# set :format, :airbrussh

# You can configure the Airbrussh format using :format_options.
# These are the defaults.
# set :format_options, command_output: true, log_file: "log/capistrano.log", color: :auto, truncate: :auto

# Default value for :pty is false
set :pty, true

# Default value for :linked_files is []
# append :linked_files, "config/database.yml"

# Default value for linked_dirs is []
# append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "public/system"

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for local_user is ENV['USER']
# set :local_user, -> { `git config user.name`.chomp }

# Default value for keep_releases is 5
# set :keep_releases, 5

# Uncomment the following to require manually verifying the host key before first deploy.
# set :ssh_options, always: :secure

# Set server address
ask(:server_address, "crucible.omargarcia.mx")